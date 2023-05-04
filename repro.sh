#!/bin/sh

set -eu

export TZ=UTC
printf "============\n${TZ}\n============\n"
echo "Creating credential in ${TZ} timezone."
python -c "import repro;repro.export_cred()"
python -c "import repro;repro.print_existing_cred()"

export TZ=America/Los_Angeles

printf "============\n${TZ}\n============\n"

echo "Creating credential in ${TZ} timezone."
python -c "import repro;repro.export_cred()"
python -c "import repro;repro.print_existing_cred()"

printf "============\n${TZ} with expired credentials\n============\n"

echo "Creating expired credential in ${TZ} timezone."
python -c "import repro;repro.export_expired_cred()"
python -c "import repro;repro.print_existing_cred()"

printf "============\n${TZ} with expired credentials created in UTC\n============\n"

echo "Checking time to expiration against expired credential created in UTC but used in ${TZ}."

export TZ=UTC
python -c "import repro;repro.export_expired_cred()"
export TZ=America/Los_Angeles
python -c "import repro;repro.print_existing_cred()"

