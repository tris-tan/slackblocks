from slackblocks import OverflowMenu, Option, SectionBlock


def make_options() -> list[Option]:
    the_options = ["Option A", "Option B"]
    return [Option(text=option, value=option) for option in the_options]

def test_basic_overflow_block() -> None:
    overflow = OverflowMenu(action_id="overflow_action", options=make_options())
    block = SectionBlock("Hello, world!",
                         block_id="fake_block_id",
                         accessory=overflow)
    print(block)

test_basic_overflow_block()