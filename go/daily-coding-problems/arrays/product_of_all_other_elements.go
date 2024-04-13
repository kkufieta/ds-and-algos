package arrays

// productOfAllOtherElements takes an array of integers and returns a new array
// such that each element at index i of the new array is the product of all the
// numbers in the original array except the one at i.
func productOfAllOtherElements(a []int) []int {
	if len(a) <= 1 {
		return a
	}

	// Get all the prefixes & suffixes
	prefixes, suffixes := []int{}, []int{}
	prefix, suffix := 1, 1

	// Get all the prefixes
	for _, el := range a {
		prefix *= el
		prefixes = append(prefixes, prefix)
	}

	// Get all the suffixes
	for i := len(a) - 1; i >= 0; i-- {
		suffix *= a[i]
		suffixes = append(suffixes, suffix)
	}
	for i, j := 0, len(suffixes)-1; i < j; i, j = i+1, j-1 {
		suffixes[i], suffixes[j] = suffixes[j], suffixes[i]
	}

	// Get & return the result
	result := []int{}
	for i := 0; i < len(a); i++ {
		p, s := 1, 1
		if i != 0 {
			p = prefixes[i-1]
		}
		if i != len(a)-1 {
			s = suffixes[i+1]
		}
		result = append(result, p*s)
	}
	return result
}
