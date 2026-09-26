import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * AURELIS Ludic Engine — Java implementation.
 * Mirrors the JS and Python engines' outputs exactly.
 */
public final class Ludic {

    private Ludic() {}

    public static List<Integer> sieve(int n) {
        List<Integer> result = new ArrayList<>();
        if (n < 1) return result;

        result.add(1);
        if (n == 1) return result;

        int cap = Math.max(n * 20, 128);
        List<Integer> working = new ArrayList<>(cap - 1);
        for (int i = 2; i <= cap; i++) working.add(i);

        while (!working.isEmpty()) {
            int stride = working.get(0);
            if (stride > n) break;
            result.add(stride);

            List<Integer> next = new ArrayList<>(working.size());
            for (int i = 1; i < working.size(); i++) {
                if (i % stride != 0) next.add(working.get(i));
            }
            working = next;
        }

        List<Integer> filtered = new ArrayList<>();
        for (int v : result) if (v <= n) filtered.add(v);
        return filtered;
    }

    public static void main(String[] args) {
        int[] inputs = {2, 3, 5, 20, 26};
        List<List<Integer>> expected = Arrays.asList(
            Arrays.asList(1, 2),
            Arrays.asList(1, 2, 3),
            Arrays.asList(1, 2, 3, 5),
            Arrays.asList(1, 2, 3, 5, 7, 11, 13, 17),
            Arrays.asList(1, 2, 3, 5, 7, 11, 13, 17, 23, 25)
        );

        for (int i = 0; i < inputs.length; i++) {
            List<Integer> got = sieve(inputs[i]);
            String status = got.equals(expected.get(i)) ? "OK " : "FAIL";
            System.out.printf("[%s] ludic(%d) = %s%n", status, inputs[i], got);
        }
    }
}
