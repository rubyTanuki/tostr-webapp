// style.css is loaded via a <link> in index.html (render-blocking, no FOUC)

// Split any .text-bouncy element into per-letter spans so the wobble
// animation (see style.css) can be staggered letter by letter.
function splitBouncyText() {
  document.querySelectorAll<HTMLElement>('.text-bouncy').forEach((el) => {
    const text = el.textContent ?? ''
    el.textContent = ''
    Array.from(text).forEach((char, i) => {
      const span = document.createElement('span')
      // non-breaking space so gaps don't collapse between inline-block spans
      span.textContent = char === ' ' ? ' ' : char
      span.style.setProperty('--i', String(i))
      el.appendChild(span)
    })
  })
}

splitBouncyText()
