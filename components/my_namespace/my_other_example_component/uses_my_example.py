import datetime

from my_namespace.my_example_component import Companies


def to_iso_time(
    *datetime_part: int, tzinfo: datetime.tzinfo = datetime.timezone.utc
) -> datetime.datetime:
    """Convert to datetime with the standard ISO format.

    Returns
    -------
    datetime
        A datetime object from datetime parts with optional timezone.

    """
    return datetime.datetime(*datetime_part, tzinfo=tzinfo)


companies_data = [
    Companies(
        "76b6defa-cc6c-4844-aaf3-5724dd60957a",
        "I",
        96,
        "Citrix",
        "disabled",
        "custom_subscriber",
        1000,
        274,
        to_iso_time(2023, 6, 30, 4, 0),
        to_iso_time(2018, 11, 21, 11, 34, 1, 512706),
        to_iso_time(2023, 7, 1, 5, 0, 13, 48587),
        to_iso_time(2022, 6, 30, 4, 0),
        "Register now!",
        "<iframe width='560' height='315' src='https://www.youtube.com/embed/BtrCTCMtNg0'\n      frameborder='0' allow='autoplay; encrypted-media' allowfullscreen></iframe>",
        '<p><strong>Congratulations! You are just steps away from having unlimited access to\xa0Boardroom Insiders\' database of 19,000+ in-depth Executive Profiles (</strong><a href="%5C" target="_self"><strong>sample</strong></a><strong>).\xa0</strong></p>\n<ol>\n<li>Complete the form to the left, then click "submit".\xa0</li>\n<li>You will automatically be logged in to the Boardroom Insiders website.\xa0</li>\n<li>Your email address will be the Username, and a unique Password will be sent to the email address you provided.\xa0</li>\n</ol>\n<p>Changing your password is simple. \xa0After logging in, click "Edit My Account" in the top right of the page. \xa0</p>\n<p>If you have any questions, please contact <a href="%5C" target="_self">Customer Service</a>.\xa0</p>\n<p>Watch this short video to learn how we\'re ideal for <strong><em>exec sales call prep</em></strong>, <strong><em>account planning</em></strong>, and <strong><em>identifying bigger deals</em></strong>.</p>\n',
        0,
        "66dc2cdbb413c3bc787b4766f4d701b5",
        "true",
        None,
        0,
        17,
        None,
        "false",
        "false",
        "false",
        40280,
        "citrix",
        157,
        to_iso_time(2024, 5, 29, 13, 55, 24),
        to_iso_time(2024, 7, 5, 6, 48, 38, 64386),
        "6fc5377f-e15d-4818-8213-02c4b9d0d856",
        to_iso_time(2024, 7, 5, 6, 40, 22),
    ),
    Companies(
        "52b4cd1b-53aa-413a-a5ba-9cd81372cf0f",
        "I",
        97,
        "BI Demo Page",
        "active",
        "custom_subscriber",
        20,
        1388,
        to_iso_time(2099, 2, 21, 5, 0),
        to_iso_time(2018, 11, 21, 11, 34, 1, 556246),
        to_iso_time(2021, 1, 18, 14, 8, 52, 764409),
        to_iso_time(2017, 2, 21, 5, 0),
        "Register Now!",
        '<iframe width="560" height="315" src="https://www.youtube.com/embed/NDMYb2HENbk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        '<p><strong>Congratulations! You are just steps away from having unlimited access to\xa0Boardroom Insiders\' database of 19,000+ in-depth Executive Profiles (</strong><a href="self_registration/15/Custom-Subscriber-/https:/www.boardroominsiders.com/view_free_profile.php" target="_blank"><strong>sample</strong></a><strong>).\xa0</strong></p>\n<ol>\n<li>Complete the form to the left, then click "submit".\xa0</li>\n<li>You will automatically be logged in to the Boardroom Insiders website.\xa0</li>\n<li>Your email address will be the Username, and a unique Password will be sent to the email address you provided.\xa0</li>\n</ol>\n<p>Changing your password is simple. \xa0After logging in, click "Edit My Account" in the top right of the page. \xa0</p>\n<p>If you have any questions, please contact\xa0<a href="mailto:customerservice@boardroominsiders.com?subject=Boardroom Insiders Customer Service" target="_blank">Customer Service</a>.\xa0</p>\n<p>Watch this short video to learn how we\'re ideal for\xa0<strong><em>exec sales call prep</em></strong>, <strong><em>account planning</em></strong>, and\xa0<strong><em>identifying bigger deals</em></strong>.</p>\n',
        0,
        "de800ea7f22b4281351cb58faf738b0d",
        "true",
        None,
        0,
        18,
        0,
        "false",
        "true",
        "true",
        None,
        "bi-demo-page",
        157,
        to_iso_time(2024, 5, 29, 13, 55, 24),
        to_iso_time(2024, 7, 5, 6, 48, 38, 64386),
        "6fc5377f-e15d-4818-8213-02c4b9d0d856",
        to_iso_time(2024, 7, 5, 6, 40, 22),
    ),
]
