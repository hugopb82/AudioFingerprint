for f in ogg/*.ogg;
do ffmpeg -i "$f" -acodec pcm_s16le -ac 1 "${f%.ogg}.wav";
done