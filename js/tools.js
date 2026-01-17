export function formatISO8601Date(date) {
  let split = date.split("-");
  let d = new Date();

  d.setFullYear(Number.parseInt(split[0]));
  d.setMonth(Number.parseInt(split[1]));
  d.setDate(Number.parseInt(split[2]));

  return d.toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}
