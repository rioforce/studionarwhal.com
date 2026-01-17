import json
from datetime import date
from pathlib import Path
from typing import TypedDict


class Video(TypedDict):
    title: str
    thumbnail: str
    url: str
    profile: str
    date: str
    category: str
    age: str


def make_thumbnail_url(code: str, /) -> str:
    return f"https://i.ytimg.com/vi/{code}/maxresdefault.jpg"


def make_film_page_url(directory_path: Path, /) -> str:
    return f"https://studionarwhal.com/{directory_path.as_posix()}"


def main() -> None:
    # BASE_YT_VIDEO_URL = "https://www.youtube.com/watch?v={code}"
    recommended_videos: list[Video] = []

    for dirpath, _, _ in (Path() / "films").walk():
        # If we're not in an individual film directory, we have nothing to do
        if dirpath.as_posix().count("/") < 2:
            continue

        # If the film lacks a info file, skip it and move on
        video_info_file = Path(dirpath) / "film-info.json"
        if not video_info_file.exists():
            print(
                f"Film located at {str(dirpath)!r} lacks a `film-info.json` file, skipping..."
            )
            continue

        # Extract the film info and restructure it for recommendation
        video_info = json.loads(video_info_file.read_text())
        recommended_videos.append(
            Video(
                title=video_info["title"],
                thumbnail=make_thumbnail_url(video_info["youtubeLink"]),
                url=make_film_page_url(dirpath),
                profile=video_info["profile"],
                date=date.fromisoformat(video_info["date"]).strftime("%b %d, %Y"),
                category=video_info.get("category", ""),
                age=video_info.get("age", ""),
            )
        )

    # Write the new recommended videos file for displaying on pages
    (Path("js") / "recommended-videos.json").write_text(
        json.dumps({"videos": recommended_videos})
    )


if __name__ == "__main__":
    main()
