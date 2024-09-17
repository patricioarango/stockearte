package services;

import com.arango.dssdg16.detos.RoleDTO;

public interface IRoleService {
    public RoleDTO findById(int id) throws Exception;
}
