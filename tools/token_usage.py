GPT5_MINI_INPUT_PRICE = 0.25 / 1_000_000
GPT5_MINI_OUTPUT_PRICE = 2.00 / 1_000_000

def get_billable_tokens(result):

    total_input = 0
    total_output = 0

    for msg in result.get("messages", []):

        usage = getattr(
            msg,
            "usage_metadata",
            None
        )

        if usage:

            total_input += usage.get(
                "input_tokens",
                0
            )

            total_output += usage.get(
                "output_tokens",
                0
            )

    return {
        "input_tokens": total_input,
        "output_tokens": total_output,
        "total_tokens": total_input + total_output
    }

def get_estimated_cost(result):

    total_input = 0
    total_output = 0

    for msg in result.get("messages", []):

        usage = getattr(
            msg,
            "usage_metadata",
            None
        )

        if usage:

            total_input += usage.get(
                "input_tokens",
                0
            )

            total_output += usage.get(
                "output_tokens",
                0
            )

    cost = (
        total_input * GPT5_MINI_INPUT_PRICE
    ) + (
        total_output * GPT5_MINI_OUTPUT_PRICE
    )

    return f"${cost:.6f}"