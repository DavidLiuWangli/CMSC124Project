HAI
	WAZZUP
		I HAS A choice
		I HAS A input
	BUHBYE

	BTW if w/o MEBBE, 1 only, everything else is invalid
	VISIBLE "1. Compute age"
	VISIBLE "2. Compute tip"
	VISIBLE "3. Compute square area"
	VISIBLE "0. Exit"

	VISIBLE "Choice: "
	GIMMEH choice

	choice IS NOW A NUMBR

	BOTH SAEM choice AN 1
	O RLY?
		YA RLY
			VISIBLE "Enter birth year: "
			GIMMEH input
			BOTH SAEM input AN "2003"
			O RLY?
				YA RLY
					VISIBLE "Isaac's birthyear!"
				MEBBE NOT BOTH SAEM input AN "2003"
					VISIBLE "Not Isaac's birthyear!"
			OIC
			VISIBLE DIFF OF 2022 AN input
	OIC

	DIFFRINT BIGGR OF 3 AN choice AN 3
	O RLY?
		YA RLY
			VISIBLE "Invalid input is > 3."
	OIC

KTHXBYE



