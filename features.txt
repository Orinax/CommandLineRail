## What to work on next:
### 28 Aug. 2024
Instead of waiting for all trains to reach their destinations before departing again, all trains should be able to
depart from their new station after a brief pause to let off and pick up new passengers.

It may not be possible to do that if going the route of always displaying progress bars on the main screen.
What if an option screen was created to allow the conductor to choose to see the progress bars of all stations?
The main difference between what is happening now would be to take away the display of how many passengers are
embarking and disembarking (the two printed lines before and after the bars). Instead of doing that, update the
numbers live on the train info table.

For that, check out: https://rich.readthedocs.io/en/stable/live.html