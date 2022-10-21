import logging
import os
import subprocess
import json

from . import interface
from .. import formats

log = logging.getLogger(__name__)

def check_output(args, env=None, sp=subprocess):
    """Call an external binary and return its stdout."""
    log.debug('calling %s with env %s', args, env)
    p = sp.Popen(args=args, env=env, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, text=True)
    (output, error) = p.communicate()
    log.info('output: %r', output)
    if error:
        log.error('error: %r', error)
    return output

def request_cmd(cmd_id, payload):
    result = check_output(["cy-cli", cmd_id, payload, cmd_id]).splitlines()
    for line in result:
        if '"commandType"' in line:
            return json.loads(line)

class X1Wallet(interface.Device):
    """Connection to X1 Wallet device."""

    @classmethod
    def package_name(cls):
        """Python package name (at PyPI)."""
        return 'x1wallet-agent'

    def connect(self):
        """Enumerate and connect to the first USB HID interface."""
        result = request_cmd("100", "00")
        return True

    def close(self):
        return

    def pubkey(self, identity, ecdh=False):
        result = bytes.fromhex(request_cmd("101", '00000000')['data'])
        log.debug('%r', result)
        return formats.decompress_pubkey(pubkey=result, curve_name=identity.curve_name)

    def sign(self, identity, blob):
        result = bytes.fromhex(request_cmd("103", '00000000' + blob.hex())['data'])
        log.debug('%r', result)
        assert len(result) == 65
        assert result[:1] == b'\x00'
        return result[1:]

    def ecdh(self, identity, pubkey):
        result = bytes.fromhex(request_cmd("102", '00000000' + pubkey)['data'])
        log.debug('%r', result)
        assert len(result) == 65
        assert result[:1] == b'\x04'
        return result
