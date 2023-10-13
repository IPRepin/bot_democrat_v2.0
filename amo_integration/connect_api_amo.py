"""
Модуль подключения к АМО CRM
"""

from amocrm.v2 import tokens


def connect_amo():
    tokens.default_token_manager(
        client_id="831a98f2-657a-4742-94b2-baf905ecc771",
        client_secret="cxeJS7e3NgqZXRt6L3Q5xfiX3YRFU7GZD6tsT7KFlYiCJPCD94YW8gvHm6eei8D4",
        subdomain="demokratnn19",
        redirect_url="https://demokrat-nn.ru/",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )

    # tokens.default_token_manager.init(code="def5020031a7ee118b1baeeadf85c42e22ae2d863bf877ec63636189d4b1225942ece26c6ec4554a001398e636ea4368eb7220490cb2e55da2e7d0b2b3a09d5dbb9fe9fa14f105f815bc6c672d44046ce2be3bca67554279cabec5f5ae1b9746d271e67a525a2916de831a940c3ed99c58549c80e9002f6381383d9021d58209fb74fb3c7f6539d4885f328d285f31dbfc0d8b0e9496f6b8ce6d520d33436d5813b57227d28bad9bfd93fb91880b6f021455cd5edd42a89ba272e4a61ba98abed859d00aa8c5463f57e2a1b39e2779d33f74842c89590c639bb44c92271bce6897c5dc7462f991e08c91d09ae00a81911f859c904fff9e2e17930c44bcba21d1c9dc152c1d27ed19ef3eeca2ca9bd4612e88818f9471ee7288ebd3f39bc25ca52cd8de45b15c2ae84f42665ad3e879b2ca7cd7cd9bf9a48271a106aa25cbc97aa2f993eff3c787cacc8c4a095b962ded711acccdea0dbf7f73d227af2b499d7650610e8d486d142338a4261a8cd11ed53ed17e4897d65dd5376bfac29177630dd905cea9de48e0349482f40650e325b929ea2c68804be1462455d9d1d41a9e8f158936d60eccd07fc89cbcc9aac33e195b76bf917a37c45f6decebfa07ee15d7b575cc21279044506b697b90a7ec192c3443b532e329900e13453204e2c99727384a38d228c6868c",
    #                                   skip_error=False)
