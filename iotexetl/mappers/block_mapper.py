# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from iotexetl.utils.string_utils import base64_string
import json

def map_block(response):
    header = response.blocks[0].block.header
    # body = response.block.body
    # footer = response.block.footer

    block = {
        'type': 'block',
        'version': header.core.version,
        'height': header.core.height,
        'timestamp': header.core.timestamp.ToJsonString(),
        'prev_block_hash': base64_string(header.core.prevBlockHash),
        'tx_root': base64_string(header.core.txRoot),
        'receipt_root': base64_string(header.core.receiptRoot),
        'delta_state_digest': base64_string(header.core.deltaStateDigest),
        'producer_pubkey': base64_string(header.producerPubkey),
        'signature': base64_string(header.signature),
    }

    return block