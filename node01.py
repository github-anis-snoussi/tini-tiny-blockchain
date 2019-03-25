#!/usr/bin/python

from flask import Flask
from flask import request
node = Flask(__name__)

this_nodes_transactions = []

@node.route('/txion', methods=['POST'])
def transaction():
  if request.method == 'POST':
    new_txion = request.get_json()
    this_nodes_transactions.append(new_txion)
    print "New transaction"
    print "FROM: {}".format(new_txion['from'])
    print "TO: {}".format(new_txion['to'])
    print "AMOUNT: {}\n".format(new_txion['amount'])
    return "Transaction submission successful\n"

node.run()

