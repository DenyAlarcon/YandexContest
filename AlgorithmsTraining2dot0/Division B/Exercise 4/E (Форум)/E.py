import sys

test_number = 1

def main():
    numbers_topics = {}
    topics_messages_counts = {}
    with open(f"{sys.path[0]}/input{test_number}.txt", encoding = 'utf-8') as f:
        N = int(f.readline().strip())
        for i in range(N):
            message_number = int(f.readline().strip())
            if message_number == 0:
                topic = f.readline().strip()
                numbers_topics[i + 1] = topic
                topics_messages_counts[topic] = 0
                message_number = i + 1
            numbers_topics[i + 1] = numbers_topics[message_number]
            topics_messages_counts[numbers_topics[message_number]] += 1
            f.readline().strip()
    
    max_messages_count = 0
    for topic in topics_messages_counts:
        current_messages_count = topics_messages_counts[topic]
        if current_messages_count > max_messages_count:
            max_messages_count = current_messages_count

    topic_with_max_messages_count = ""
    for topic in topics_messages_counts:
        if topics_messages_counts[topic] == max_messages_count:
            topic_with_max_messages_count = topic
            break

    with open(f"{sys.path[0]}/output{test_number}.txt", "w", encoding = 'utf-8') as f:
        f.write(topic_with_max_messages_count)


if __name__ == "__main__":
    main()
