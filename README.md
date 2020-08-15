# KanTeX

KanTeX is a library that allow you to layout and format text using python. It is mainly intended to be used with Telegram Userbots and Bots.

KanTeX defaults to markdown but can be switched to using html by using `from kantex.html import *`. To be explicit about using Markdown, `from kantex.md import *` can be used. 

## Examples

```python
from kantex.md import *

doc = KanTeXDocument(
    Section('A Section',
            Italic('A italic Text'),
            Mention('Telegram', 777000)))
print(doc)
```

Result:

```markdown
**A Section**
    __A italic Text__
    [Telegram](tg://user?id=777000)
```

---

```python
from kantex.html import *

doc = KanTeXDocument(
    Section('A Section',
            Italic('A italic Text'),
            Mention('Telegram', 777000)))
print(doc)
```

Result:

```html
<b>A Section</b>
    <i>A italic Text</i>
    <a href="tg://user?id=777000">Telegram</a>
```

---

```python
from kantex.md import *

doc = KanTeXDocument()
for i in range(5):
    sec = Section(f'Section {i}')
    for n in range(2):
        sec.append(KeyValueItem(i, n))
    doc.append(sec)


print(doc)
```

Result:
```markdown
**Section 0**
    0: 0
    0: 1

**Section 1**
    1: 0
    1: 1

**Section 2**
    2: 0
    2: 1

**Section 3**
    3: 0
    3: 1

**Section 4**
    4: 0
    4: 1
```

---

```python
from kantex import *

doc = KanTeXDocument(
    Section('Nested',
            SubSection('Sections',
                       Italic('work too'))))

print(doc)
```

Result:

```markdown
**Nested**
    **Sections**
        __work too__
```
