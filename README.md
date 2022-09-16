# Summary
This is just to showcase some testing practices from an academic project. Implementation of the command line Shogi game was originally created by and forked from [here](https://github.com/Urbistondo/Shogi). 

Below is a sample of certain tests used. Download the ***test report*** for more information on other coverage criterias used and the classes they covered.

# Example

Test for ValidateMoveService.py

Class covered: ValidateMoveService

Coverage criteria used: All-uses

Coverage obtained: 100%

Testing steps: 

Class consisted of mostly if statements with exceptions raised within each if statement. Because of the layout of the code in this class, all-use coverage criteria seemed reasonable to use. In order to cover all uses within the test file, a test was created for each instance where an exception could be raised. This includes exceptions OriginSquareEmptyException, OriginSquareContainsEnemyPieceException, DestinationSquareOccupiedException, InvalidMovementForPieceException, and PieceMovementPathObstructedException (these are all exceptions created by the author of this repo). Variables board, origin_coordinates, destination_coordinates, and color were all defined in node 1. Their uses varied slightly however, with color only being used within some if statements, and board, origin_coordinates, and destination_coordinates being used for every if statement.  

Since all exceptions were covered and passed, 100% coverage was obtained.

[![image.png](https://i.postimg.cc/zfs1mcRw/image.png)](https://postimg.cc/mcynCVjh)
