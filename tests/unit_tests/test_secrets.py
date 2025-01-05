from langchain_pipeshift import ChatPipeshift  # PipeshiftEmbeddings


def test_chat_pipeshift_secrets() -> None:
    o = ChatPipeshift(pipeshift_api_key="foo")  # type: ignore[call-arg]
    s = str(o)
    assert "foo" not in s
