#!/bin/bash

ip="10.10.206.139"
low=13000
high=13999

while [ $low -le $high ]; do
  mid=$(((low + high) / 2))
  echo "[*] Trying port $mid"

  out=$(ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -p $mid -oBatchMode=yes -oConnectTimeout=3 $ip 2>&1)

  if echo "$out" | grep -q "Higher"; then
    echo "[+] Server says: Go higher"
    low=$((mid + 1))
  elif echo "$out" | grep -q "Lower"; then
    echo "[+] Server says: Go lower"
    high=$((mid - 1))
  else
    echo "[-] Found a different response (possible correct port or error):"
    echo "$out"
    break
  fi
done
