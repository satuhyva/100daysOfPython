# IN TERMINAL:

# to get env vars:
# env

# to set env var:
# export TEST_ENV_VAR=JIPPII

import os
test_env_var = os.environ.get("TEST_ENV_VAR")
print(test_env_var)
print(os.environ.get("TEST_TRUTH") == 'True')

test_env_var = os.getenv("TESTVAR")
print(test_env_var)

# WHY ONLY THIS WORKS???
# ilmeisesti Terminal sulkeutuu ja sinne asetettu tieto sitten katoaa
# on voimassa vain siinä bashissa, jossa on asetettu...
test_env_var = os.getenv("LOGNAME")
print(test_env_var)


