from klefki.crypto.ecdsa import pubkey
from klefki.types.algebra.concrete import (
    EllipticCurveGroupSecp256k1 as ECG,
    FiniteFieldSecp256k1 as F
)
from klefki.types.algebra.isomorphism import bijection, do


def encode_pubkey(key: ECG):
    x = hex(key.value[0].value)[2:]
    y = hex(key.value[1].value)[2:]
    return '0' * (32 - len(x)) + x + '0' * (32 - len(y)) + y


@bijection(encode_pubkey)
def decode_pubkey(key: str) -> ECG:
    x = F(int(key[:32], 16))
    y = F(int(key[32:], 16))
    return ECG((x, y))


gen_pub_key = do(
    encode_pubkey,
    pubkey
)