import textwrap

sample_text = """This function wraps the input paragraph such that each line
n the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list
is empty if the wrapped
output has no content."""

wrapper = textwrap.TextWrapper(width=50)

dedented_text = textwrap.dedent(text=sample_text)
original = wrapper.fill(text=dedented_text)

print('Original:\n')
print(original)

shortened = textwrap.shorten(text=original, width=100)
shortened_wrapped = wrapper.fill(text=shortened)

print('\nShortened:\n')
print(shortened_wrapped)
