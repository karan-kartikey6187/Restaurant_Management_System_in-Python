from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.model.colors import Color

class StaffManager:
    @staticmethod
    def remove_staff():
        print(Color.YELLOW+"\n")
        print(Color.BRIGHT_BLUE+"=" * 50)
        print(Color.YELLOW+"REMOVE STAFF")
        print(Color.BRIGHT_BLUE+"=" * 50)
        
        staff_data = ReadWrite.read(Path.staff_data_path)
        if staff_data is None:
            print(Color.RED+"No staff data file found!")
            input(Color.YELLOW+"\nPress Enter...")
            return
        
        staff_list = staff_data if isinstance(staff_data, list) else staff_data.get("staff", [])
        non_admin_staff = [staff for staff in staff_list if staff.get('role') != "Admin"]
        
        if not non_admin_staff:
            print(Color.RED+"No staff members available to remove!")
            input(Color.YELLOW+"\nPress Enter...")
            return
        
        print(Color.YELLOW+"\nCurrent Staff Members (Non-Admin):")
        print(Color.BRIGHT_BLUE+"-" * 50)
        print(Color.WHITE+f"{'No':<4} {'ID':<10} {'Name':<15} {'Role':<12} {'Contact'}")
        print(Color.BRIGHT_BLUE+"-" * 50)
        
        for i, staff in enumerate(non_admin_staff):
            staff_id = staff.get('id', 'N/A')
            name = staff.get('name', 'N/A')[:14]
            role = staff.get('role', 'N/A')
            contact = staff.get('contact', 'N/A')
            print(Color.WHITE+f"{i+1:<4} {Color.CYAN}{staff_id:<10} {Color.CYAN}{name:<15} {Color.YELLOW}{role:<12} {Color.CYAN}{contact}")
        
        print(Color.BRIGHT_BLUE+"-" * 50)
        
        try:
            choice = int(input(Color.BRIGHT_BLUE+"Enter staff number to remove (0 to cancel): "+Color.YELLOW))
            
            if choice == 0:
                print(Color.YELLOW+"Cancelled.")
                input(Color.YELLOW+"\nPress Enter...")
                return
            
            if 1 <= choice <= len(non_admin_staff):
                staff_to_remove = non_admin_staff[choice-1]
                original_index = staff_list.index(staff_to_remove)
                
                staff_name = staff_to_remove.get('name', 'Unknown')
                staff_role = staff_to_remove.get('role', 'Unknown')
                
                confirm = input(Color.RED+f"\nRemove {Color.CYAN}{staff_name} ({Color.YELLOW}{staff_role})? (y/n): "+Color.YELLOW).lower()
                
                if confirm in ['y', 'yes']:
                    staff_list.pop(original_index)
                    ReadWrite.write_json(staff_list, Path.staff_data_path)
                    print(Color.GREEN+f"\n✓ {Color.CYAN}{staff_name} removed successfully!")
                else:
                    print(Color.YELLOW+"Cancelled.")
            else:
                print(Color.RED+"Invalid selection!")
                
        except ValueError:
            print(Color.RED+"Please enter a valid number!")
        except Exception as e:
            print(Color.RED+f"Error: {e}")
        
        input(Color.YELLOW+"\nPress Enter...")
