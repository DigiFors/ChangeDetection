import pytest
from src.ChangeDetection.relationship_detection import RelationshipDetection


@pytest.mark.parametrize(
    "old, new, result, works",
    [
        ("abcd", "abcdz", ['=a', '=b', '=c', '=d', '+z'], True),
        ("abcd", "abzcd", ['=a', '=b', '+z', '=c', '=d'], True),
        ("abcd", "dbca", ['+d', '+b', '+c', '=a', '-b', '-c', '-d'], True),
        ("abcd", "dbca", ['+d', '+b', '+c', '=a', '-b', '-c', '-d'], True),
        ("aabb", "aazbb", ['=a', '=a', '+z', '=b', '=b'], True),
        ("affe", "apfel affe", ['=a', '=a', '+z', '=b', '=b'], True),

    ]
)
def test_detection(old, new, result, works: bool):
    detection = RelationshipDetection()
    changes = detection.detect(old, new)
    if works:
        assert changes == result
    else:
        assert changes != result

    detection.print()


test = """<body class="home page-template page-template-full_width page-template-full_width-php page page-id-331 locale-de-de qode-title-hidden qode_grid_1300 footer_responsive_adv qode-child-theme-ver-1.0.0 qode-theme-ver-16.2.1 qode-theme-bridge usm-premium-15.9-updated-2021-08-05 wpb-js-composer js-comp-ver-6.7.0 vc_responsive" itemscope="" itemtype="http://schema.org/WebPage">
<div class="wrapper">
<div class="wrapper_inner">
<!-- Google Analytics start -->
<!-- Google Analytics end -->
<header class="scroll_header_top_area stick scrolled_not_transparent page_header">
<div class="header_inner clearfix">
<form action="https://digifors.de/" class="qode_search_form" id="searchform" method="get" role="search">
<div class="container">
<div class="container_inner clearfix">
"""

test2 = """<body>
<div class="signin">
<a class="button" href="https://accounts.google.com/ServiceLogin?hl=de&amp;cd=DE&amp;continue=https://www.google.de/&amp;gae=cb-">Anmelden</a>
</div>
<div class="box">
<img alt="Google" height="28" src="//www.gstatic.com/images/branding/googlelogo/1x/googlelogo_color_68x28dp.png" srcset="//www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_68x28dp.png 2x" width="68"/><div class="productLogoContainer">
<img alt="" aria-hidden="true" class="image" height="100%" src="https://www.gstatic.com/ac/cb/scene_cookie_wall_search_v2.svg" width="100%"/>
</div>"""


def test_body():
    detection = RelationshipDetection()
    old = test
    new = test2
    detection.detect(old, new)
    print(" ")
    detection.print()
    print(" ")
    print(" ")
    assert False
