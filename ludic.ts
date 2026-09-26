/**
 * AURELIS Ludic Engine — TypeScript implementation.
 * Full type safety across the sieve pipeline.
 */

export type LudicList = readonly number[];

export interface LudicResult {
  readonly bound: number;
  readonly values: LudicList;
  readonly count: number;
  readonly elapsedMs: number;
}

export class LudicEngine {
  static sieve(bound: number): number[] {
    const n = Math.trunc(Number(bound));
    if (!Number.isFinite(n) || n < 1) return [];

    const result: number[] = [1];
    if (n === 1) return result;

    const cap = Math.max(n * 20, 128);
    let working: number[] = [];
    for (let i = 2; i <= cap; i++) working.push(i);

    while (working.length > 0) {
      const stride = working[0];
      if (stride > n) break;
      result.push(stride);

      const next: number[] = [];
      for (let i = 1; i < working.length; i++) {
        if (i % stride !== 0) next.push(working[i]);
      }
      working = next;
    }

    return result.filter((v) => v <= n);
  }

  static measure(bound: number): LudicResult {
    const t0 = performance.now();
    const values = LudicEngine.sieve(bound);
    const t1 = performance.now();
    return {
      bound,
      values,
      count: values.length,
      elapsedMs: Number((t1 - t0).toFixed(4)),
    };
  }
}

/* --- Test harness (Node) --- */
const cases: Array<[number, number[]]> = [
  [2, [1, 2]],
  [3, [1, 2, 3]],
  [5, [1, 2, 3, 5]],
  [20, [1, 2, 3, 5, 7, 11, 13, 17]],
  [26, [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]],
];

for (const [n, expected] of cases) {
  const got = LudicEngine.sieve(n);
  const ok = JSON.stringify(got) === JSON.stringify(expected);
  console.log(`[${ok ? "OK " : "FAIL"}] ludic(${n}) = [${got.join(", ")}]`);
}
