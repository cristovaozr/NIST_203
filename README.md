# NIST_FIPS.203
Implementation of the NIST.203 specification for the KEM

## About this repository

This repository contains a simple implementation of the NIST FIPS.203 Key Encapsulation Mechanism (KEM), which is based on the Ring-LWE problem.

There are two main parts to this repository:
* The `mlkem` folder, which contains the implementation in Python. And
* The `app` folder, which contains two programs: `alice.py` and `bob.py`

To execute a key exchange using this method, one instance must run the `bob.py` app and another instance should run the `alice.py` app.

For now, `bob` should be run first, so that Alice can connect to it and the exchange should occur smoothly.

## Running the apps

To run `bob` you must do:
```bash
PYTHONPATH=. ./apps/bob.py -p apps/bob_params.json -a ALICE_IP_ADDRESS:26287
```

To run `alice` you must do:
```bash
PYTHONPATH=. ./apps/alice.py -p apps/alice_params.json -a BOB_IP_ADDRESS:2602
```

## Params file

This file contains the parameters that `alice` and `bob` uses. It also contains the port which to listen to, so this can be customized.

### File `alice_params.json`

This file contains two parameters: `d` and `z` which should be generated randomly in runtime. For now, these are set to a fixed value but, in the future, omitting these keys should make the app generate them on-the-fly.

### File `bob_params.json`

This file contains the parameter `m`, which should be generated randomly in runtime. For now, this is set to a fixed vale but, in the future, omitting this key should make the app generate it on-the-fly.

## Future work

A few things are still pending:
- [ ] Auto generation of the `d`, `z` and `m` parameters on-the-fly
- [ ] Complete the implementation of the MLKEM as described by FIPS.203 (for now only the main behavior is complete)
- [ ] Review documentation and fill in the gaps

