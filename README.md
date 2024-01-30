# [Industrial Relations Club](https://industrialrelations.club/) 📟
This single-serve website is designed for doctors in training (DiT) working in Western Australia’s public hospitals. Our [agreement](https://www.amawa.com.au/wp-content/uploads/2022/09/WA-Health-System-Medical-Practitioners-AMA-Industrial-Agreement-2022.pdf) with the government is quite difficult to read, so I made this site to clearly and easily tell doctors how much money they should be making on any day of the week.

You can see it live now at [https://industrialrelations.club/](https://industrialrelations.club/).

For each DiT pay scale, it provides a breakdown of the:
- Annual salary
- Penalty rates
- Professional development allowance
- Leave entitlements
- Recall rates
- Meal allowances

The site is based on publicly available information in the [AMA WA Industrial Agreement (2022)](https://www.amawa.com.au/wp-content/uploads/2022/09/WA-Health-System-Medical-Practitioners-AMA-Industrial-Agreement-2022.pdf) and the [WA Government's New Wage Policy (2022)](https://web.archive.org/web/20230604183824/https://www.wa.gov.au/organisation/department-of-treasury/wages-policy).

When the new agreement is negotiated, a manual update will be required. Salaries will automatically be incremented according to the terms set out in the New Wage Policy (2022) until then.

## Inspiration
When the new interns start every year, there is invariably a deluge of questions to more senior doctors about penalty rates. What if I work on a Saturday? What about recall rates? What if it's a full moon?

In 2024, I was lucky enough to be married to one of those interns and unlucky enough to field many such payslip questions. Having forgotten exactly what the penalty rates were myself, I made this site to obviate the need for further interrogation.

## Shift Calculator
The shift calculator applies the penalty terms in the Agreement to a single shift and tells you how much you should be paid for it. There are two major shortcomings…

- **Public holiday** management has not yet been implemented (due to programmer lassitude).
- **Overtime** is not accounted for because only one shift is entered at a time. This is primarily a user interface design issue. The underlying code is designed to calculate the value of multiple shifts at a time.

This project has given me quite a bit of sympathy for the poor souls at [HSS](https://www.hss.health.wa.gov.au/) who had to implement this *with other peoples’ real money*. I can only imagine how un-fun it would be to write this in COBAL.

## Open Source
Industrial Relations Club makes use of these open source projects:
- [Twemoji](https://github.com/twitter/twemoji) for the pager (📟) favicon (CC-BY 4.0 License)
    - Converted to .ico via [favicon.io](https://favicon.io/)
- [Feather](https://github.com/feathericons/feather) for the icons (MIT License)