import os
import sys

import repository

try:
    param1 = sys.argv[1]
    program = sys.argv[2]
    key = sys.argv[3]

    if param1 == 'set':
        pass
    elif param1 == 'get':
        os.system('vaultctl -u >> /dev/null')
        value = repository.get_kv(program, key)
        print(value)
        os.system('vaultctl -s >> /dev/null')
    elif param1 == 'test':
        pass
    else:
        raise IndexError
except IndexError:
    print('Opção inválida.')
