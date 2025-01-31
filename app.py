import gradio as gr
import os

# 🔹 ฟังก์ชันคำนวณจำนวนซอง
def calculate_pouches(repeat_length, total_meters, num_lenses):
    if repeat_length and total_meters and num_lenses:
        try:
            pouches = (total_meters * 1000 * num_lenses) / repeat_length
            pouches = int(pouches)  # ตัดจุดทศนิยม
            return f"📦 จำนวนซองที่ได้: {pouches:,} ซอง"  # ใส่ลูกน้ำให้ตัวเลขอ่านง่าย
        except ZeroDivisionError:
            return "⚠️ ไม่สามารถหารด้วย 0 ได้ กรุณากรอกค่าที่ถูกต้อง"
    return "⚠️ กรุณากรอกข้อมูลให้ครบทุกช่อง"

# 🔹 ฟังก์ชันเคลียร์ค่า
def clear_inputs():
    return None, None, None, ""

# 🔹 CSS ปรับ UI
css = """
#output_box {
    font-size: 22px !important;
    font-weight: bold;
    color: #007BFF;
}
"""

# 🔹 สร้าง Web App
with gr.Blocks(css=css) as demo:
    gr.Markdown("# 🏭 โปรแกรมคำนวณจำนวนซอง")
    gr.Markdown("### 🔢 กรอกค่าที่ต้องการ แล้วกด '🔥 คำนวณ' เพื่อดูผลลัพธ์")

    repeat_length = gr.Number(label="📏 ระยะ Repeat (มม.)")
    total_meters = gr.Number(label="📏 จำนวนเมตร (ม.)")
    num_lenses = gr.Number(label="🔲 จำนวนเลนส์")

    with gr.Row():
        calculate_button = gr.Button("🔥 คำนวณ")
        clear_button = gr.Button("♻️ เคลียร์ค่า")

    output_result = gr.Textbox(label="📌 ผลลัพธ์", lines=2, interactive=False, elem_id="output_box")

    calculate_button.click(
        fn=calculate_pouches,
        inputs=[repeat_length, total_meters, num_lenses],
        outputs=output_result,
    )

    clear_button.click(
        fn=clear_inputs,
        inputs=[],
        outputs=[repeat_length, total_meters, num_lenses, output_result],
    )

# 🔹 เปิดใช้งาน Web App บน Render
port = int(os.getenv("PORT", 7860))  # ดึงค่า PORT จาก Render
demo.launch(server_name="0.0.0.0", server_port=port)
