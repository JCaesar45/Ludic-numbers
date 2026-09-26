function ludic(n) {
  if (n < 1) return [];
  
  const result = [1];
  if (n === 1) return result;
  
  // Generate a sufficiently large initial array
  // We need enough numbers to survive the sieving process
  // A safe upper bound is roughly n * some factor, but let's be generous
  let limit = Math.max(n * 10, 100);
  let arr = [];
  for (let i = 2; i <= limit; i++) {
    arr.push(i);
  }
  
  while (arr.length > 0) {
    const L = arr[0];
    
    // If the next ludic number exceeds n, we can stop
    if (L > n) break;
    
    result.push(L);
    
    // Remove every L-th indexed item (including the first)
    // This means keep items at indices where (index % L) !== 0
    const newArr = [];
    for (let i = 1; i < arr.length; i++) {
      if (i % L !== 0) {
        newArr.push(arr[i]);
      }
    }
    arr = newArr;
  }
  
  // Filter to only include numbers <= n (the sieve might produce some > n)
  return result.filter(x => x <= n);
}
