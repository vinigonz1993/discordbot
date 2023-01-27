import axios from 'axios';

const endpoint = process.env.REACT_API

export default {
    oct: {
        get: () => axios.get(
            `${endpoint}oct`,
            {
                method: 'GET',
                params: {
                    stopNo: 1222,
                    routeNo: 57
                },
            },
        ),
    },
};