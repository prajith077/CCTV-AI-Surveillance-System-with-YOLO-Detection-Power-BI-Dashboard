export default function Dashboard() {
  return (
    <div>
      <h1>📊 PPE Dashboard</h1>

      <iframe
        src="https://app.powerbi.com/view?r=eyJrIjoiODA4ZjdiMmUtNGExMi00NWY2LTlhZWQtYjg5OGE2M2EwNTRhIiwidCI6IjNiNmE2OTUxLTdjMmMtNGU3YS1iNWQ4LWQ3Y2ZiN2IwOWViMSJ9"
        width="100%"
        height="650"
        style={{ border: "none", marginTop: "20px" }}
      />
    </div>
  );
}