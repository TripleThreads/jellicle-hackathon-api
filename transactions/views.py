from datetime import time
from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
from flask import json
from transactions.network import Blockchain, Block


def index(request):
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)

    return HttpResponse(json.dumps({"length": len(chain_data),
                       "chain": chain_data}), mimetype='application/json')


def check_for_cache(request):
    is_cached_blocks = ('Blockchain' in request.session)
    is_cached_peers = ('Peers' in request.session)
    blockchain = Blockchain()
    peers = set()
    if is_cached_blocks:
        blockchain = request.session['Blockchain']
    if is_cached_peers:
        peers = request.session['Peers']
    return blockchain, peers


def create(request):
    blockchain, peers = check_for_cache(request)
    tx_data = request.get_json()

    required_fields = ["farmer_id", "store_id", "product_id", "status", "amount", "net_price"]

    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data", 404

    tx_data["timestamp"] = time.time()
    blockchain.add_new_transaction(tx_data)
    return "Success", 201


def mine(request):
    blockchain, peers = check_for_cache(request)
    result = blockchain.mine()
    if not result:
        return "No transactions to mine"
    return "Block #{} is mined.".format(result)


def register_new_peers(request):
    blockchain, peers = check_for_cache(request)
    nodes = request.get_json()
    if not nodes:
        return "Invalid data", 400
    for node in nodes:
        peers.add(node)

    return "Success", 201


def validate_and_add_block(request):
    blockchain, peers = check_for_cache(request)
    block_data = request.get_json()
    block = Block(block_data["index"],
                  block_data["transactions"],
                  block_data["timestamp",
                  block_data["previous_hash"]])

    proof = block_data['hash']
    added = blockchain.add_block(block, proof)

    if not added:
        return "The block was discarded by the node", 400

    return "Block added to the chain", 201


def pending(request):
    blockchain, peers = check_for_cache(request)
    return json.dumps(blockchain.unconfirmed_transactions)


def consensus(request):
    """
    Our simple consnsus algorithm. If a longer valid chain is
    found, our chain is replaced with it.
    """
    global blockchain
    blockchain, peers = check_for_cache(request)

    longest_chain = None
    current_len = len(blockchain)

    for node in peers:
        response = requests.get('http://{}/chain'.format(node))
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and blockchain.check_chain_validity(chain):
            current_len = length
            longest_chain = chain

    if longest_chain:
        blockchain = longest_chain
        return True

    return False


def announce_new_block(request, block):
    blockchain, peers = check_for_cache(request)
    """
    A function to announce to the network once a block has been mined.
    Other blocks can simply verify the proof of work and add it to their
    respective chains.
    """
    for peer in peers:
        url = "http://{}/add_block".format(peer)
        requests.post(url, data=json.dumps(block.__dict__, sort_keys=True))

