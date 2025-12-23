#!/usr/bin/env python3
"""
Example script to run IBQF experiments.

Usage:
    python run_experiment.py
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ibqf import IBQF
import numpy as np


def main():
    """Run a basic IBQF experiment."""
    print("=" * 60)
    print("IBQF Experiment Runner")
    print("=" * 60)
    
    # Configuration
    filter_size = 10000
    num_hash_functions = 3
    num_tracks = 1000
    
    print(f"\nConfiguration:")
    print(f"  Filter size: {filter_size}")
    print(f"  Hash functions: {num_hash_functions}")
    print(f"  Number of tracks: {num_tracks}")
    
    # Create filter
    print("\nCreating IBQF filter...")
    ibqf = IBQF(size=filter_size, hash_functions=num_hash_functions)
    
    # Add tracks
    print(f"Adding {num_tracks} tracks...")
    tracks = [f"track_{i}" for i in range(num_tracks)]
    for track in tracks:
        ibqf.add(track)
    
    # Calculate statistics
    occupancy = np.sum(ibqf.filter)
    occupancy_rate = 100 * occupancy / filter_size
    
    print(f"\nResults:")
    print(f"  Filter occupancy: {occupancy} / {filter_size} ({occupancy_rate:.2f}%)")
    
    # Test queries
    print("\nTesting queries...")
    true_positives = sum(1 for track in tracks if ibqf.query(track))
    print(f"  True positives: {true_positives} / {num_tracks} ({100 * true_positives / num_tracks:.1f}%)")
    
    # Test false positive rate
    false_tracks = [f"false_track_{i}" for i in range(num_tracks)]
    false_positives = sum(1 for track in false_tracks if ibqf.query(track))
    fpr = 100 * false_positives / num_tracks
    print(f"  False positives: {false_positives} / {num_tracks} ({fpr:.1f}%)")
    
    print("\n" + "=" * 60)
    print("Experiment complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
