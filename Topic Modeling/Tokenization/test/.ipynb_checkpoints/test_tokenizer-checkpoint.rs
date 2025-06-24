use crate::tokenizer::CangJieTokenizer;
use crate::options::TokenizerOption;
use jieba_rs::Jieba;

#[test]
fn test_tokenizer_cut() {
    let mut tokenizer = CangJieTokenizer {
        worker: std::sync::Arc::new(Jieba::new()),
        option: TokenizerOption::Default { hmm: true },
    };

    let stream = tokenizer.token_stream("南京市长江大桥");
    let tokens: Vec<String> = stream.map(|token| token.text.clone()).collect();

    assert!(tokens.contains(&"南京市".to_string()));
    assert!(tokens.contains(&"长江大桥".to_string()));
}
