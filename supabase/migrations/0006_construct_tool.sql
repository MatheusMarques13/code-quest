-- Adiciona Construct às ferramentas. (ALTER TYPE ADD VALUE roda fora de transação.)
alter type tool_kind add value if not exists 'construct';
