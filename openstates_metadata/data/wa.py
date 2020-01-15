from ..models import State, Chamber, District, simple_numbered_districts

WA = State(
    name="Washington",
    abbr="WA",
    capital="Olympia",
    capital_tz="America/Los_Angeles",
    fips="53",
    unicameral=False,
    legislature_name="Washington State Legislature",
    division_id="ocd-division/country:us/state:wa",
    jurisdiction_id="ocd-jurisdiction/country:us/state:wa/government",
    url="http://www.leg.wa.gov",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        num_seats=98,
        title="Representative",
        districts=[
            District("1", "lower", 2, "ocd-division/country:us/state:wa/sldl:1"),
            District("2", "lower", 2, "ocd-division/country:us/state:wa/sldl:2"),
            District("3", "lower", 2, "ocd-division/country:us/state:wa/sldl:3"),
            District("4", "lower", 2, "ocd-division/country:us/state:wa/sldl:4"),
            District("5", "lower", 2, "ocd-division/country:us/state:wa/sldl:5"),
            District("6", "lower", 2, "ocd-division/country:us/state:wa/sldl:6"),
            District("7", "lower", 2, "ocd-division/country:us/state:wa/sldl:7"),
            District("8", "lower", 2, "ocd-division/country:us/state:wa/sldl:8"),
            District("9", "lower", 2, "ocd-division/country:us/state:wa/sldl:9"),
            District("10", "lower", 2, "ocd-division/country:us/state:wa/sldl:10"),
            District("11", "lower", 2, "ocd-division/country:us/state:wa/sldl:11"),
            District("12", "lower", 2, "ocd-division/country:us/state:wa/sldl:12"),
            District("13", "lower", 2, "ocd-division/country:us/state:wa/sldl:13"),
            District("14", "lower", 2, "ocd-division/country:us/state:wa/sldl:14"),
            District("15", "lower", 2, "ocd-division/country:us/state:wa/sldl:15"),
            District("16", "lower", 2, "ocd-division/country:us/state:wa/sldl:16"),
            District("17", "lower", 2, "ocd-division/country:us/state:wa/sldl:17"),
            District("18", "lower", 2, "ocd-division/country:us/state:wa/sldl:18"),
            District("19", "lower", 2, "ocd-division/country:us/state:wa/sldl:19"),
            District("20", "lower", 2, "ocd-division/country:us/state:wa/sldl:20"),
            District("21", "lower", 2, "ocd-division/country:us/state:wa/sldl:21"),
            District("22", "lower", 2, "ocd-division/country:us/state:wa/sldl:22"),
            District("23", "lower", 2, "ocd-division/country:us/state:wa/sldl:23"),
            District("24", "lower", 2, "ocd-division/country:us/state:wa/sldl:24"),
            District("25", "lower", 2, "ocd-division/country:us/state:wa/sldl:25"),
            District("26", "lower", 2, "ocd-division/country:us/state:wa/sldl:26"),
            District("27", "lower", 2, "ocd-division/country:us/state:wa/sldl:27"),
            District("28", "lower", 2, "ocd-division/country:us/state:wa/sldl:28"),
            District("29", "lower", 2, "ocd-division/country:us/state:wa/sldl:29"),
            District("30", "lower", 2, "ocd-division/country:us/state:wa/sldl:30"),
            District("31", "lower", 2, "ocd-division/country:us/state:wa/sldl:31"),
            District("32", "lower", 2, "ocd-division/country:us/state:wa/sldl:32"),
            District("33", "lower", 2, "ocd-division/country:us/state:wa/sldl:33"),
            District("34", "lower", 2, "ocd-division/country:us/state:wa/sldl:34"),
            District("35", "lower", 2, "ocd-division/country:us/state:wa/sldl:35"),
            District("36", "lower", 2, "ocd-division/country:us/state:wa/sldl:36"),
            District("37", "lower", 2, "ocd-division/country:us/state:wa/sldl:37"),
            District("38", "lower", 2, "ocd-division/country:us/state:wa/sldl:38"),
            District("39", "lower", 2, "ocd-division/country:us/state:wa/sldl:39"),
            District("40", "lower", 2, "ocd-division/country:us/state:wa/sldl:40"),
            District("41", "lower", 2, "ocd-division/country:us/state:wa/sldl:41"),
            District("42", "lower", 2, "ocd-division/country:us/state:wa/sldl:42"),
            District("43", "lower", 2, "ocd-division/country:us/state:wa/sldl:43"),
            District("44", "lower", 2, "ocd-division/country:us/state:wa/sldl:44"),
            District("45", "lower", 2, "ocd-division/country:us/state:wa/sldl:45"),
            District("46", "lower", 2, "ocd-division/country:us/state:wa/sldl:46"),
            District("47", "lower", 2, "ocd-division/country:us/state:wa/sldl:47"),
            District("48", "lower", 2, "ocd-division/country:us/state:wa/sldl:48"),
            District("49", "lower", 2, "ocd-division/country:us/state:wa/sldl:49"),
        ],
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        num_seats=49,
        title="Senator",
        districts=simple_numbered_districts(
            "ocd-division/country:us/state:wa", "upper", 49
        ),
    ),
)
