#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$ROOT/code${PYTHONPATH:+:$PYTHONPATH}"

python "$ROOT/code/generate_witnesses.py"
python "$ROOT/code/verify_witnesses.py"
python "$ROOT/code/independent_edge_list_check.py"
python "$ROOT/code/adversarial_mutation_tests.py"
python "$ROOT/code/verify_spectral_certificate.py"

if python -c 'import sympy' >/dev/null 2>&1; then
  python "$ROOT/code/verify_spectral_certificate_sympy.py"
else
  echo "SKIP: optional SymPy cross-check (SymPy is not installed)"
fi

echo "ALL CORE CHECKS PASSED"
