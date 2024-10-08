use flowy_document2::entities::*;
use flowy_test::document::document_event::DocumentEventTest;
use flowy_test::document::utils::*;

#[tokio::test]
async fn get_document_event_test() {
  let test = DocumentEventTest::new().await;
  let view = test.create_document().await;
  let document = test.open_document(view.id).await;
  let document_data = document.data;
  assert!(!document_data.page_id.is_empty());
  assert!(document_data.blocks.len() > 1);
}

#[tokio::test]
async fn apply_document_event_test() {
  let test = DocumentEventTest::new().await;
  let view = test.create_document().await;
  let doc_id = view.id.clone();
  let document = test.open_document(doc_id.clone()).await;
  let block_count = document.data.blocks.len();
  let insert_action = gen_insert_block_action(document);
  let payload = ApplyActionPayloadPB {
    document_id: doc_id.clone(),
    actions: vec![insert_action],
  };
  test.apply_actions(payload).await;
  let document = test.open_document(doc_id).await;
  let document_data = document.data;
  let block_count_after = document_data.blocks.len();
  assert_eq!(block_count_after, block_count + 1);
}

#[tokio::test]
async fn undo_redo_event_test() {
  let test = DocumentEventTest::new().await;
  let view = test.create_document().await;
  let doc_id = view.id.clone();

  let document = test.open_document(doc_id.clone()).await;
  let insert_action = gen_insert_block_action(document);
  let payload = ApplyActionPayloadPB {
    document_id: doc_id.clone(),
    actions: vec![insert_action],
  };
  test.apply_actions(payload).await;
  let block_count_after_insert = test.open_document(doc_id.clone()).await.data.blocks.len();

  // undo insert action
  let can_undo = test.can_undo_redo(doc_id.clone()).await.can_undo;
  assert!(can_undo);
  test.undo(doc_id.clone()).await;
  let block_count_after_undo = test.open_document(doc_id.clone()).await.data.blocks.len();
  assert_eq!(block_count_after_undo, block_count_after_insert - 1);

  // redo insert action
  let can_redo = test.can_undo_redo(doc_id.clone()).await.can_redo;
  assert!(can_redo);
  test.redo(doc_id.clone()).await;
  let block_count_after_redo = test.open_document(doc_id.clone()).await.data.blocks.len();
  assert_eq!(block_count_after_redo, block_count_after_insert);
}

#[tokio::test]
async fn insert_text_block_test() {
  let test = DocumentEventTest::new().await;
  let view = test.create_document().await;
  let text = "Hello World";
  let block_id = test.insert_index(&view.id, text, 1, None).await;
  let block = test.get_block(&view.id, &block_id).await;
  assert!(block.is_some());
  let block = block.unwrap();
  let data = gen_text_block_data(text);
  assert_eq!(block.data, data);
}

#[tokio::test]
async fn update_text_block_test() {
  let test = DocumentEventTest::new().await;
  let view = test.create_document().await;
  let block_id = test.insert_index(&view.id, "Hello World", 1, None).await;
  let update_text = "Hello World 2";
  test.update(&view.id, &block_id, update_text).await;
  let block = test.get_block(&view.id, &block_id).await;
  assert!(block.is_some());
  let block = block.unwrap();
  let update_data = gen_text_block_data(update_text);
  assert_eq!(block.data, update_data);
}
