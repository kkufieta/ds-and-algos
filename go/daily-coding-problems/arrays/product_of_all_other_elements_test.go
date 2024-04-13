package arrays

import (
	"testing"

	"go.viam.com/test"
)

func TestProductOfAllOtherElements(t *testing.T) {
	testCases := []struct {
		description string
		input       []int
		output      []int
	}{
		{
			description: "empty array",
			input:       []int{},
			output:      []int{},
		},
		{
			description: "array with one value",
			input:       []int{9},
			output:      []int{9},
		},
		{
			description: "successful case",
			input:       []int{1, 2, 3, 4, 5},
			output:      []int{120, 60, 40, 30, 24},
		},
		{
			description: "successful case with array with negative elements",
			input:       []int{3, -2, 1},
			output:      []int{-2, 3, -6},
		},
	}

	for _, testCase := range testCases {
		t.Run(testCase.description, func(t *testing.T) {
			expectedOutput := productOfAllOtherElements(testCase.input)
			test.That(t, testCase.output, test.ShouldResemble, expectedOutput)
		})
	}
}
