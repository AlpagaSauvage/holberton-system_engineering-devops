# Amazon issue

## Issue Summary

Issue started the 2 October at 9pm and ended at 2 October at 11am.

The problem affected 100% of the users and prevented the possibility to buy anything on the site.

## Root Cause :
When we tried to import 500 new products into the database, we forgot to add the region condition, so to undo this, we planned to delete all the new products added, a condition was missing on the SQL line, which results in the deletion of every product.

## Timeline
The problem started on 2 October at 9am and ended on 2 October at 11am.

We detected the problem using one of our monitoring systems that we have in place.

## Action Taken
What we do first is to download the latest database backup (we make backups every night).
While the backup is being downloaded, we inform all users with a notification of the problem on the homepage.
We import the previous day's backup into the database.
The next step is the most complicated, because we have a backup from the day before, but people were able to buy our products on the day of the incident, so we have to link the purchases to the products.

## Escalate
The incident scale to the communication and moderation teams, because they have to say about the incident for people who asking.

## Corrective and preventing
To prevent the issue, we have a safety mode in MySQL Workbench, the developper desactived it because it was easier to work with out, but with it nothing about that happen.