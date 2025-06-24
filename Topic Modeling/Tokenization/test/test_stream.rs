use crate::stream::CangjieTokenStream;
use tantivy::tokenizer::Token;

#[test]
fn test_token_stream_behavior() {
    let input = "中国人民";
    let segments = vec!["中国", "人民"];
    let mut stream = CangjieTokenStream::new(input, segments);

    let mut tokens = vec![];
    while stream.advance() {
        let token = stream.token().clone();
        tokens.push(token.text);
    }

    assert_eq!(tokens, vec!["中国", "人民"]);
}
