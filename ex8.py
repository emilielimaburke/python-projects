formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.", 
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

## The last line outputs with single and double quotes because
## of the single quotes in `didn't` in the third line!