# personal-finance
**Preview 0.2**

An application to help the user with personal finance and financial literacy.

It is capable of the following functions at the moment:
* configuring currency and income
* tracking your spendings
* tracking your savings
* searching your added spendings/savings line
* summarizing your savings and spendings, and calculating left-over from your income

Upcoming features:
* New Period button for storing left-over as savings and starting with same income as previously
* date for spendings/savings lines
* About window for detailed usage

Known issues:
* 0 value in summarized values show up as 'None'
* summarized values are not refreshed
* summarized values should be stored in new table
* income is not summarized from income lines
* savings is not summarized from savings lines
* configured income is not pulled automatically when adding an income line (salary/wage)
* no currency symbols for each line of spending/saving
* somewhat ugly UI
* listbox is not well organized
* modifying values without selection throws NameError
* modifying after refresh or delete gets the previously selected value
* empty string values and values with dashes in them have curly brackets
* search function needs to be improved

Technologies used:

* Backend: Python (sqlite3 library)
* Frontend: Python (tkinter library)
