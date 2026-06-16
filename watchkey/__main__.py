#!/usr/bin/env python3
"""
watchkey/__main__.py
Command-line interface for watchkey.

Usage:
  python -m watchkey encrypt --seed "word1 word2 ... word24" --out vault.json
    python -m watchkey decrypt --vault vault.json
      python -m watchkey demo
      """

      import argparse
      import sys

      from .core import encrypt_seed, decrypt_seed, save_vault, load_vault
      from .simulator import simulate_samples


      def cmd_encrypt(args):
          print("[watchkey] Collecting biometric samples from Apple Watch…")
              print("           (using simulator — replace with real HealthKit export)")
                  samples = simulate_samples(n=30)
                      print(f"           {len(samples)} samples collected.")

                          vault = encrypt_seed(args.seed, samples)
                              save_vault(vault, args.out)
                                  print(f"[watchkey] ✓ Vault saved to {args.out}")
                                      print("           Your seed phrase is now