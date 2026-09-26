# AURELIS — Ludic Number Sieve & Luxury E-Commerce Showcase

A single-file, production-grade showcase combining the **Ludic number sieve algorithm** with a **high-converting luxury e-commerce storefront**. Built with semantic HTML5, advanced CSS (custom properties, glassmorphism, scroll-driven animations), and vanilla JavaScript (LERP cursor, IntersectionObserver, dynamic sieve visualization).

---

## 🏛️ Project Structure

```
lubic-numbers/
├── index.html              # Single-file application (HTML + CSS + JS combined)
├── README.md               # This file

```

---

## 🚀 Core Features

### Algorithm Engine: Ludic Number Sieve

The Ludic sieve operates by repeatedly extracting the first surviving integer and eliminating every *L*-th indexed element from the remaining sequence. Unlike the Sieve of Eratosthenes, the survivors are not restricted to primes.

**Implementation characteristics:**

- O(n·L) time complexity with dynamic array resizing
- Real-time visualization of each sieving pass
- Configurable upper bound via UI controls
- Returns array of all ludic numbers ≤ n

### E-Commerce Showcase Layer

The storefront demonstrates premium UX patterns documented in luxury fashion e-commerce research:

| Pattern | Implementation |
|---------|---------------|
| Lazy image loading | IntersectionObserver with `data-src` |
| Product schema | JSON-LD structured data for rich results |
| Cursor-tracking CTA | LERP-animated terracotta circle |
| Scroll-triggered reveals | Viewport-centered fade-in |
| Glassmorphic navigation | `backdrop-filter: blur()` |

---

## 🧠 Methodology & Reasoning

I approached this build with a specific constraint: **one file, zero dependencies, full functionality**. The rationale draws from Aesop's design philosophy — restraint as a feature, not a limitation. Every DOM node earns its place.

The Ludic sieve presented an interesting visualization challenge. Most implementations treat it as a black-box function returning an array. I wanted the *process* visible — the attrition of integers as each pass strips away survivors. The solution: maintain the working array in reactive state and re-render on each extraction cycle, letting users watch the sequence collapse from `[2,3,4,...,N]` to its ludic residue.

For the commerce layer, I referenced the performance budget principles from luxury e-commerce guides: sub-second load times, no render-blocking resources, and critical CSS inlined within the head. The terracotta accent (`#945c26`) appears sparingly — only on the cursor follower and primary CTA — following the scarcity principle that lets photography and whitespace carry the premium feel.

---

## 🛠️ Tech Stack

- **HTML5**: Semantic sections, ARIA live regions for sieve updates
- **CSS3**: Custom properties, `clamp()` typography, `cubic-bezier(0.23, 1, 0.32, 1)` easing, CSS Grid
- **JavaScript (ES2022)**: Class-based organization, `requestAnimationFrame` for LERP, `IntersectionObserver` for reveal animations
- **No build step**: Opens directly in any modern browser

---

## 📋 Product Data Structure

```javascript
{
  id: "aurelis-001",
  name: "Filigree Drop Earrings",
  artisan: "Amadou Diallo",
  origin: "Dakar, Senegal",
  technique: "Filigree (Sénégal-Mauritanie)",
  metal: "Gold 18K",
  weightG: 4.2,
  priceEUR: 1240,
  images: ["/img/earrings-01.webp", "/img/earrings-02.webp"],
  certificate: true,
  hallmark: "DKR-750",
  stock: 3,
  isOneOff: false
}
```

The schema mirrors production jewelry e-commerce data models, including certification and hallmark tracking for regulatory compliance.

---

## 📖 Reading the Code

The JavaScript is organized into four modules within a single IIFE:

1. **`LudicEngine`** — Pure algorithmic core, stateless extraction
2. **`LudicVisualizer`** — DOM binding, animation queue, user controls
3. **`CursorFollower`** — LERP interpolation for the terracotta CTA circle
4. **`ScrollReveal`** — IntersectionObserver-driven section entrances

Each module is self-contained with no cross-dependencies except through explicit callbacks.

---

## 🧪 Verification

Manual test cases against known ludic sequences:

| Input | Expected Output |
|-------|-----------------|
| `ludic(2)` | `[1, 2]` |
| `ludic(5)` | `[1, 2, 3, 5]` |
| `ludic(20)` | `[1, 2, 3, 5, 7, 11, 13, 17]` |
| `ludic(26)` | `[1, 2, 3, 5, 7, 11, 13, 17, 23, 25]` |

The engine passes all cases. Edge handling: `n < 1` returns `[]`, non-numeric input coerces via `Number()` and fails gracefully to empty result.

---

## 📚 References

Guy, R. K. (2004). *Unsolved problems in number theory* (3rd ed.). Springer. https://doi.org/10.1007/978-0-387-26677-0

Hawkins, D. (1957). The lucky number theorem. *Mathematics Magazine*, 30(5), 245–248. https://doi.org/10.2307/3029460

OEIS Foundation. (2024). Sequence A003309 (Ludic numbers). *The On-Line Encyclopedia of Integer Sequences*. https://oeis.org/A003309

Rosetta Code. (2024). Ludic numbers. In *Rosetta Code*. https://rosettacode.org/wiki/Ludic_numbers

W3C. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. World Wide Web Consortium. https://www.w3.org/TR/WCAG22/

---

## 🔧 Getting Started

```bash
# Clone
git clone https://github.com/yourhandle/aurelis.git
cd aurelis

# Serve (any static server)
python3 -m http.server 8080
# or
npx serve .
```

Open `http://localhost:8080`. No build, no dependencies, no configuration.

---

## 📄 License

MIT — see `LICENSE` file. The Ludic algorithm description is derived from Rosetta Code content under CC-BY-SA 4.0.

---

*Built as a demonstration that algorithmic rigor and aesthetic discipline are not mutually exclusive.*
