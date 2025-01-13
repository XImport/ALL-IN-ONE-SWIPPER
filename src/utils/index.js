import * as XLSX from "xlsx";

export function exportToExcel(data, filename = "data.xlsx") {
  // Create a new workbook
  const workbook = XLSX.utils.book_new();

  // Convert your data array to a worksheet
  const worksheet = XLSX.utils.json_to_sheet(data);

  // Append the worksheet to the workbook
  XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");

  // Write the workbook and trigger the download
  XLSX.writeFile(workbook, filename);
}
