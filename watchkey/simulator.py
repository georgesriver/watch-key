"""
watchkey/simulator.py
Simulates Apple Watch biometric data for development and testing.

In production, replace this with real HealthKit / CoreMotion data
exported from your WatchOS companion app.
"""

import math
import random
import time
from typing import List, Optional

from .core import BiometricSample


def simulate_samples(
    n: int = 30,
        base_hr: float = 72.0,
            seed: Optional[int] = None,
            ) -> List[BiometricSample]:
                """
                    Generate *n* simulated Apple Watch samples.

                        Parameters
                            ----------
                                n        : number of samples (>= 10 required by encrypt_seed)
                                    base_hr  : resting heart rate BPM to simulate around
                                        seed     : fix random seed for reproducible tests
                                            """
                                                rng = random.Random(seed)
                                                    now = 1_700_000_000.0 if seed is not None else time.time()
                                                        samples = []

                                                            for i in range(n):
                                                                    t = now + i * 0.5          # 500 ms apart (typical Watch polling)
                                                                            hr = base_hr + rng.gauss(0, 2.5)

                                                                                    # Simulate wrist resting on a table — small residual motion
                                                                                            ax = rng.gauss(0.0, 0.05)
                                                                                                    ay = rng.gauss(0.0, 0.05)
                                                                                                            az = rng.gauss(-9.81, 0.05)   # gravity on Z

                                                                                                                    gx = rng.gauss(0.0, 0.01)
                                                                                                                            gy = rng.gauss(0.0, 0.01)
                                                                                                                                    gz = rng.gauss(0.0, 0.01)

                                                                                                                                            samples.append(BiometricSample(
                                                                                                                                                        timestamp=t,
                                                                                                                                                                    heart_rate_bpm=hr,
                                                                                                                                                                                accel_x=ax, accel_y=ay, accel_z=az,
                                                                                                                                                                                            gyro_x=gx,  gyro_y=gy,  gyro_z=gz,
                                                                                                                                                                                                    ))

                                                                                                                                                                                                        return samples