package pythagorean

type Triplet [3]int

// Range generates list of all Pythagorean triplets with side lengths
// in the provided range.
func Range(min, max int) []Triplet {

	var TripletReturn []Triplet
	for i := min; i < max; i++ {
		for j := min; j < max; j++ {
			for new_max := max; new_max > 0; new_max-- {
				if new_max*new_max == i*i+j*j && i < j {
					newTriplet := [3]int{i, j, new_max}
					TripletReturn = append(TripletReturn, newTriplet)
				}
			}
		}
	}

	return TripletReturn
	panic("Please implement the Range function")
}

// Sum returns a list of all Pythagorean triplets with a certain perimeter.
func Sum(p int) []Triplet {
	var propTriplet []Triplet
	var newTriplet []Triplet = Range(1, p-1)
	for i := 0; i < len(newTriplet); i++ {
		if newTriplet[i][0]+newTriplet[i][1]+newTriplet[i][2] == p {
			propTriplet = append(propTriplet, newTriplet[i])
		}
	}
	return propTriplet
}
