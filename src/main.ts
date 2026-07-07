// style.css is loaded via a <link> in index.html (render-blocking, no FOUC)

// Split any .text-bouncy element into per-letter spans so the wobble
// animation (see style.css) can be staggered letter by letter.
// Letters are grouped into .bouncy-word wrappers so lines can only
// wrap at the spaces between words, never mid-word.
function splitBouncyText() {
  document.querySelectorAll<HTMLElement>('.text-bouncy').forEach((el) => {
    const text = (el.textContent ?? '').trim().replace(/\s+/g, ' ')
    el.textContent = ''
    let i = 0
    text.split(' ').forEach((word, w) => {
      if (w > 0) {
        el.appendChild(document.createTextNode(' '))
        i++ // count the space so the ripple stays continuous across words
      }
      const wordSpan = document.createElement('span')
      wordSpan.className = 'bouncy-word'
      Array.from(word).forEach((char) => {
        const span = document.createElement('span')
        span.textContent = char
        span.style.setProperty('--i', String(i++))
        wordSpan.appendChild(span)
      })
      el.appendChild(wordSpan)
    })
  })
}

splitBouncyText()
