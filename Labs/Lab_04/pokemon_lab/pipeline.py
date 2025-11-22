#!/usr/bin/env python3

import sys
import update_portfolio
import generate_summary

def run_production_pipeline():
    print("Starting production pipeline...", file=sys.stderr)
    print("\n--- Running Portfolio Update ---", file=sys.stderr)
    update_portfolio.main()

    print("\n--- Running Portfolio Summary Generation ---", file=sys.stderr)
    generate_summary.main()

    print("\n--- Production pipeline completed ---", file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()